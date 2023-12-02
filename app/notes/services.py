from datetime import datetime

from app.core.exceptions import CannotAddDataToDatabase
from app.core.logger import logger
from app.notes.schemas import Note
from app.notes.dao import NoteDAO
from app.users.schemas import User


async def add_new_note(note: Note, user: User) -> int:
    if not note.create_at:
        note.create_at = datetime.now()

    new_note_id = await NoteDAO.add(
        user_id=user.id,
        create_at=note.create_at,
        text=note.text,
    )

    if not new_note_id:
        raise CannotAddDataToDatabase

    return new_note_id


async def get_all_user_notes(user: User) -> list[Note]:
    return await NoteDAO.find_all(user_id=user.id)


logger.info(msg='init notes services')
