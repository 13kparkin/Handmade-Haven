from flask import Blueprint
from app.models import Review

review_routes = Blueprint("review", __name__)


@review_routes.route("/<int:id>")
def ReviewsPage(id):
    """ "get users reviews"""

    User_Reviews = Review.query.filter(Review.user_id == id).all()
    return [review.to_dict() for review in User_Reviews]
