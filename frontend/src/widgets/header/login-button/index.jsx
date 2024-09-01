import React from "react"
import { NavLink } from "react-router-dom"

const LoginButton = () => {
  return (
    <div className="login-button">
      <NavLink to={"/"}>
        <div className="nav-item">Login</div>
      </NavLink>
    </div>
  )
}

export default LoginButton
