import React from "react"
import { NavLink } from "react-router-dom"
import "./styles.scss"

const MainCategories = ({ activeIndex, setActiveIndex, categories }) => {
  const setNavItemActiveId = (index) =>
    activeIndex === index ? " nav-item-active" : ""

  return (
    <ul className="main-categories">
      {categories.map((category, idx) => (
        <li key={idx} onClick={() => setActiveIndex(category.index)}>
          <NavLink to={category.path}>
            <div
              className={`nav-item nav-item-hover${setNavItemActiveId(category.index)}`}
            >
              {category.name}
            </div>
          </NavLink>
        </li>
      ))}
    </ul>
  )
}

export default MainCategories
