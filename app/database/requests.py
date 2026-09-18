from app.database.models import async_session, User, Category, Card
from sqlalchemy import select, update

async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()
            return False
        return True if user.name else False

async def get_user(tg_id):
    async with async_session() as session:
        return await session.scalar(select(User).where(User.tg_id == tg_id))


async def update_user(tg_id, name, phone_number):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(name=name,
                                                                             phone_number=phone_number))
        await session.commit()

async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))

async def get_cards_by_category(category_id):
    async with async_session() as session:
        return await session.scalars(select(Card).where(Card.category_id == category_id))

async def get_card(card_id):
    async with async_session() as session:
        return await session.scalar(select(Card).where(Card.id == card_id))