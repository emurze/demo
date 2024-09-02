import React from "react"
import "./styles.scss"
import TeacherMiniCard from "../../entities/teacher-mini-card"

const TeachersPhotoLine = () => {
  return (
    <div className="teachers-photo-line">
      <h2 className="teachers-photo-line__title">
        This is the place where you can find basic information about your
        teachers.
      </h2>
      <div className="teachers-photo-line__body">
        <TeacherMiniCard />
      </div>
    </div>
  )
}

export default TeachersPhotoLine
