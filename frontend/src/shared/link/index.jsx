import React from "react"
import { NavLink } from "react-router-dom"
import "./styles.scss"

const MyNavLink = ({ to, children }) => {
  return (
    <span className="link">
      <NavLink to={to}>{children}</NavLink>
    </span>
  )
}

export default MyNavLink
