import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useModal } from "../../context/Modal";
import { Rating } from "react-simple-star-rating";
import { UpdateReviewThunk, getReviewsByUser } from "../../store/reviews";

function UpdateReviewsModal({ Review }) {
  const dispatch = useDispatch();
  // let origReview = useSelector(state => state.reviews.LoggedInUsersReviews[reviewId])
  let [review, setReview] = useState(Review.comment);
  let [rating, setRating] = useState(Review.stars);
  let user_id = useSelector((state) => state.session.user.id);
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();

  // Catch Rating value
  const handleRating = (rate) => {
    setRating(rate);
    // Some logic
  };
  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors([]);
    let Errors = [];
    if (review.length < 30) {
      Errors.push("Reviews must be 30 Characters or more!!");
    }
    if (review.length > 500) {
      Errors.push("Reviews must be 500 Characters or less!!");
    }
    if (rating < 0 || rating > 5) {
      Errors.push("Ratings Are Positive Numbers Under 5!!");
    }
    if (!Errors.length) {
      dispatch(
        UpdateReviewThunk({ id: Review.id, comment: review, stars: rating })
      );
      closeModal();
    } else {
      setErrors(Errors);
    }
  };
  return (
    <>
      <div className="modal-Review">
        <h1 className="review-header">Update Review</h1>
        <form className="ReviewForm" onSubmit={handleSubmit}>
          <ul>
            {errors.map((error, idx) => (
              <li className="ReviewsErrors" key={idx}>
                {error}
              </li>
            ))}
          </ul>

          <textarea
            className="text-review"
            placeholder={"How was your Purchase?"}
            value={review}
            onChange={(e) => setReview(e.target.value)}
          />

          <Rating onClick={handleRating} ratingValue={rating}></Rating>

          <button className="ReviewButton dropdown-button" type="submit">
            Update Review
          </button>
        </form>
      </div>
    </>
  );
}

export default UpdateReviewsModal;
