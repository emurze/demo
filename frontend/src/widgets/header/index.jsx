import React from "react"
import "./styles.css"
import Logo from "../../shared/logo"
import MainCategories from "./main-categories"
import LoginButton from "./login-button"

const Header = () => {
  const categories = [
    { name: "Home", path: "/" },
    { name: "Teachers", path: "/teachers" },
    { name: "Subjects", path: "/subjects" },
  ]

  return (
    <header className="header">
      <div className="header__container">
        <Logo />
        <MainCategories categories={categories} />
        <LoginButton />
      </div>
    </header>
  )
}

export default Header
