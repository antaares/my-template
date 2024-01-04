from aiogram.dispatcher.filters.state import StatesGroup, State



class AdminState(StatesGroup):
    """States of admins"""

    # broadcast
    getMessage = State()
    Choice = State()
    Confirm = State()

    # manage channels
    ForwardingMessage = State()
    ChannelID = State()
    ChannelDeleteConfirm = State()