from controllers.dashboard_controller import DashboardController
from core.database import get_session_context
from fastapi import APIRouter, Depends
from schemas.dashboard_schema import DashboardCardData
from sqlmodel.ext.asyncio.session import AsyncSession

router = APIRouter(
    prefix="/dashboards",
    tags=["Dashboard"],
)


@router.get(
    "/cards",
    summary="Get data for cards.",
    response_model=DashboardCardData,
)
async def get_cards_data(
    db_manager: AsyncSession = Depends(get_session_context),
):
    return await DashboardController(db_manager).get_cards_data()
