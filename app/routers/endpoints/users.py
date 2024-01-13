from fastapi import APIRouter

router = APIRouter()

instituteList = [
    {
        "institute_id": "institute_asdjakjdkdjlkadknlndladasdj311123",
        "created_date": "Dec 19 2023 08:47:42 GMT+0530",
        "updated_date": "Dec 20 2023 08:47:42 GMT+0530",
        "name": "The Buddhist international school",
        "address": "Radhakrushna nagar, Yavatmal",
        "State": "MH",
        "city": "YTL",
        "email": "buddhistschool@gmail.com",
        "contact": "9898989899"
    },
    {
        "institute_id": "institute_asdjakjdkdjlkadknlndladasdj3119876",
        "created_date": "Dec 18 2023 08:47:42 GMT+0530",
        "updated_date": "Dec 20 2023 08:47:42 GMT+0530",
        "name": "The Potdar international school",
        "address": "Radhika nagar, Yavatmal",
        "State": "MH",
        "city": "YTL",
        "email": "potdarschool@gmail.com",
        "contact": "9797979797"
    }
]

@router.get("/", tags=["users"])
async def read_users():
    return instituteList


@router.get("/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}