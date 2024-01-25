from core.logger import get_logger
from repositories.articles_repository import ArticlesReposotiry
from repositories.articles_statuses_repository import (
    ArticlesStatusesReposotiry,
)
from repositories.projects_repository import ProjectsReposotiry
from repositories.settings_repository import SettingsReposotiry
from schemas.dashboard_schema import (
    ArticleCard,
    DashboardCardData,
    DashboardNetworkStatusesData,
    DashboardStatusesData,
    NetworkCard,
    ProjectCard,
)
from sqlmodel.ext.asyncio.session import AsyncSession

logger = get_logger(__name__)


class DashboardController:
    def __init__(self, db_manager: AsyncSession):
        self.db_manager = db_manager

    async def get_cards_data(self) -> DashboardCardData:
        async with self.db_manager as session:
            articles = await ArticlesReposotiry(
                session
            ).retrieve_all_articles()

            published = [
                article for article in articles if article.network_statuses
            ]
            published_count = len(published)

            with_error_count = sum(
                1
                for article in published
                if any(
                    status.status != "DONE"
                    for status in article.network_statuses
                )
            )

            projects = await ProjectsReposotiry(
                session
            ).retrieve_all_project_objects()

            settings = await SettingsReposotiry(
                session
            ).retrieve_unique_settings()

        return DashboardCardData(
            articles=ArticleCard(
                total=len(articles),
                published=published_count,
                with_error=with_error_count,
            ),
            projects=ProjectCard(total=len(projects)),
            networks=NetworkCard(total=len(settings)),
        )

    async def get_statuses_data(self) -> list[DashboardStatusesData]:
        async with self.db_manager as session:
            published_articles_id = await ArticlesStatusesReposotiry(
                session
            ).retrieve_last_id_articles_statuses()
            articles = await ArticlesReposotiry(
                session
            ).retrieve_article_by_list_id(published_articles_id)

            results = [
                DashboardStatusesData(
                    date=article.published[0].created,
                    project_name=article.project.name,
                    article_id=article.id,
                    article_title=article.title,
                    network_statuses=[
                        DashboardNetworkStatusesData(
                            id=publish.id,
                            name=publish.networks_setting.name,
                            status=publish.status,
                            status_text=publish.status_text,
                        )
                        for publish in article.published
                    ],
                )
                for article in articles
            ]

            results = sorted(results, key=lambda x: x.date, reverse=True)

            return results
