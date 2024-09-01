import React from "react"
import { NavLink } from "react-router-dom"
import "./styles.scss"

const Logo = () => {
  return (
    <div className="logo">
      <NavLink to={"/"}>
        <div className="nav-item">Logo</div>
      </NavLink>
    </div>
  )
}

export default Logo
