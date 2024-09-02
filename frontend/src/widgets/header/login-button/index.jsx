import React from "react"
import { NavLink } from "react-router-dom"
import "./styles.scss"

const LoginButton = ({ index, activeIndex, setActiveIndex }) => {
  const navItemActiveString = activeIndex === index ? " nav-item-active" : ""

  return (
    <div className={"login-button"} onClick={() => setActiveIndex(index)}>
      <NavLink to={"/"}>
        <div className={`nav-item-hover nav-item${navItemActiveString}`}>
          Login
        </div>
      </NavLink>
    </div>
  )
}

export default LoginButton
