import React, { useState } from "react"
import "./styles.css"
import Logo from "../../shared/logo"
import MainCategories from "./main-categories"
import LoginButton from "./login-button"

const Header = () => {
  const [activeIndex, setActiveIndex] = useState(0)
  const categories = [
    { name: "Home", path: "/", index: 1 },
    { name: "Teachers", path: "/teachers", index: 2 },
    { name: "Subjects", path: "/subjects", index: 3 },
    { name: "Schedule", path: "/schedule", index: 4 },
  ]
  const loginButtonIndex = 5

  return (
    <header className="header">
      <div className="header__container">
        <div onClick={() => setActiveIndex(0)}>
          <Logo />
        </div>
        <MainCategories
          activeIndex={activeIndex}
          setActiveIndex={setActiveIndex}
          categories={categories}
        />
        <LoginButton
          index={loginButtonIndex}
          activeIndex={activeIndex}
          setActiveIndex={setActiveIndex}
        />
      </div>
    </header>
  )
}

export default Header
