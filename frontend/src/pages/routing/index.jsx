import React from "react"
import { Route, Routes } from "react-router-dom"
import HomePage from "../home-page"
import Page404 from "../page-404"
import TeachersPage from "../teachers-page"
import SubjectsPage from "../subjects-page"

const Routing = () => {
  return (
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/teachers" element={<TeachersPage />} />
      <Route path="/subjects" element={<SubjectsPage />} />
      <Route path="*" element={<Page404 />} />
    </Routes>
  )
}

export default Routing
