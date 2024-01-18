import models
from sqlalchemy.orm import Session




def get_user(db: Session, user_id: int):

    """
    Get User by id.

    Return_type:
        User | None
    """

    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):

    """
    Get User by username

    Return_type:
        User | None
    """

    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session):

    """
    Get List Of Users

    Return_type:
        User | None
    """
    
    return db.query(models.User).all()




def get_filtered_users(db: Session, city: str | None, country: str | None, age: int | None):

    """
    Get Filtered Users
    Filter By age
    Filter By city
    Filter By Country
    And Combinations of these.
    In case all filters above not matching, return all users objects.

    Return_type:
        List[User]
    """

    if city and country and age:
        return db.query(models.User).filter(models.User.city == city).filter(models.User.country == country).filter(models.User.age == age).all()

    elif city and country and not age:
        return db.query(models.User).filter(models.User.city == city).filter(models.User.country == country).all()
    
    elif city and age and not country:
        return db.query(models.User).filter(models.User.city == city).filter(models.User.age == age).all()
    
    elif city and not country and not age:
        return db.query(models.User).filter(models.User.city == city).all()
    
    elif country and age and not city:
        return db.query(models.User).filter(models.User.country == country).filter(models.User.age == age).all()

    elif country and not city and not age:
        return db.query(models.User).filter(models.User.country == country).all()
    
    elif age and not city and not country:
        return db.query(models.User).filter(models.User.age == age).all()

    else:
        return db.query(models.User).all()
