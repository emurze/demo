import React from "react"
import "./styles.css"
import { NavLink } from "react-router-dom"

const Header = () => {
  const categories = [
    { name: "Home", path: "/" },
    { name: "Teachers", path: "/teachers" },
    { name: "Subjects", path: "/subjects" },
  ]

  return (
    <header className="header">
      <div className="header__container">
        <NavLink to={"/"}>
          <div className="logo nav-item">Logo</div>
        </NavLink>
        <ul className="categories">
          {categories.map((category, idx) => (
            <li key={idx}>
              <NavLink to={category.path}>
                <div className="nav-item">{category.name}</div>
              </NavLink>
            </li>
          ))}
        </ul>
        <NavLink to={"/"}>
          <div className="account nav-item">Login</div>
        </NavLink>
      </div>
    </header>
  )
}

export default Header
