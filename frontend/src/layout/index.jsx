import React from "react"
import Header from "../widgets/header"
import "./styles.scss"

const Layout = ({ children }) => {
  return (
    <>
      <Header />
      <main className="main">{children}</main>
    </>
  )
}

export default Layout
