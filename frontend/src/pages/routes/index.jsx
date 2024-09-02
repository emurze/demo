import React from "react"
import { Route, Routes as ReactRoutes } from "react-router-dom"
import HomePage from "../home-page"
import Page404 from "../page-404"
import TeachersPage from "../teachers-page"
import SubjectsPage from "../subjects-page"
import TeacherDetailsPage from "../teacher-details-page"

const Routes = () => {
  return (
    <ReactRoutes>
      <Route path="/" element={<HomePage />} />
      <Route path="/teachers" element={<TeachersPage />} />
      <Route path="/teachers/:id" element={<TeacherDetailsPage />} />
      <Route path="/subjects" element={<SubjectsPage />} />
      <Route path="*" element={<Page404 />} />
    </ReactRoutes>
  )
}

export default Routes
