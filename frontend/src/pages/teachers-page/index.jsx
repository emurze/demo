import React from "react"
import Teachers from "../../widgets/teachers"
import AddTeacher from "../../features/add-teacher/ui"

const TeachersPage = () => {
  return (
    <div className="teachers-page">
      <AddTeacher />
      <Teachers />
    </div>
  )
}

export default TeachersPage
