import React from "react"
import { NavLink } from "react-router-dom"
import "./styles.scss"

const Logo = () => {
  return (
    <NavLink to={"/"}>
      <div className="logo">Logo</div>
    </NavLink>
  )
}

export default Logo
