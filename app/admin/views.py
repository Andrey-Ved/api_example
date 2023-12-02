from sqladmin import ModelView

from app.core.logger import logger
from app.notes.models import Notes
from app.users.models import Users


class UsersAdmin(ModelView, model=Users):
    column_details_exclude_list = [
        Users.hashed_password,
    ]
    column_list = [
        Users.name,
        Users.email,
        Users.full_name,
    ]
    column_labels = {
        Users.name: "Name",
        Users.email: "E-mail",
        Users.full_name: "Full name",
    }
    column_sortable_list = [Users.name]
    can_delete = False

    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"


class NotesAdmin(ModelView, model=Notes):
    @staticmethod
    def date_format(model, attribute):
        return getattr(model, attribute).strftime(
            "%Y.%m.%d %H:%M:%S"
        )

    column_list = [
        Notes.user,
        Notes.create_at,
        Notes.text,
    ]
    column_labels = {
        Notes.user: "Name",
        Notes.create_at: "Create at",
        Notes.text: "Text",
    }
    column_formatters = {Notes.create_at: date_format}

    name = "Note"
    name_plural = "Notes"
    icon = "fa-solid fa-notes"

    page_size = 50
    page_size_options = [25, 50, 100, 200]


logger.info(msg='init sqladmin views')
