import React from "react"
import { useParams } from "react-router-dom"
import TeacherDetailsCard from "../../entities/teacher-details-card"

const TeacherDetailsPage = () => {
  const { id } = useParams()

  console.log(id)

  return (
    <div className="teacher-details-page">
      Details page
      <TeacherDetailsCard productId={id} />
    </div>
  )
}

export default TeacherDetailsPage
