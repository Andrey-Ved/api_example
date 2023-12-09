from fastapi import APIRouter, Depends
from fastapi_versioning import version
from typing import Annotated

from app.core.logger import logger
from app.notes.schemas import Note, NotesList
from app.notes.services import get_all_user_notes, add_new_note
from app.users.schemas import User
from app.users.services import get_current_active_user


router = APIRouter(
    prefix="/notes",
    tags=["Notes"],
)


@router.post("/post-note")
@version(1)
async def post_note(
        new_note: Note,
        current_user: Annotated[User, Depends(get_current_active_user)],
) -> Note:
    await add_new_note(new_note, current_user)
    return new_note


@router.get("/get-all")
@version(2)
async def get_all_my_notes(
        current_user: Annotated[User, Depends(get_current_active_user)],
) -> NotesList:
    return NotesList(
        data = await get_all_user_notes(current_user)
    )


logger.info(msg='init notes routers')
