import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { getUserCart, addItemToCart, updateItemInCart, deleteFromCart } from "../../store/shoppingcart"
// import { addNewOrder } from "../../store/orders"
import "./shoppingcart.css"

export default function ShoppingCart() {
  const dispatch = useDispatch();
  const cart = useSelector((state) => state?.cart?.cart);
  console.log("cart items", cart)
  const currUser = useSelector((state) => state?.session?.user)
  console.log("current user", currUser)

  useEffect(() => {
    dispatch(getUserCart())
  }, [dispatch])

  if (!currUser) {
    return (
      <div className="cart-container">
        <h1>Please log in to add items to cart</h1>
      </div>
    );
  }


  const updateHandler = async (e, item) => {
    const itemData = {
      id: item.id,
      userId: currUser.id,
      productId: item.product_id,
      quantity: (e.target.value)
    }
    await dispatch(updateItemInCart(itemData))
  }

  const deleteHandler = async (e, item) => {
    e.preventDefault()
    const itemData = {
      id: item.id,
      userId: currUser.id,
      productId: item.product_id
    }
    await dispatch(deleteFromCart(itemData))
  }


  const cartQuantity = (cartArr) => {
    let total = 0
    for (let item of cartArr) {
      total += item.quantity
    }
    return total
  }

  const cartPrice = (cartArr) => {
    let total = 0
    for (let item of cartArr) {
      let itemPrice = item.quantity * item.product.price
      total += itemPrice
    }
    return total
  }

  return (
    <h1>Welcome to your Shopping Cart</h1>
  )
}
