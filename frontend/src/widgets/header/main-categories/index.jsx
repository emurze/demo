import React from "react"
import { NavLink } from "react-router-dom"
import "./styles.scss"

const MainCategories = ({ categories }) => {
  return (
    <ul className="main-categories">
      {categories.map((category, idx) => (
        <li key={idx}>
          <NavLink to={category.path}>
            <div className="nav-item">{category.name}</div>
          </NavLink>
        </li>
      ))}
    </ul>
  )
}

export default MainCategories
