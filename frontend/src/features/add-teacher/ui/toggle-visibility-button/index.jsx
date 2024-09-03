import React from "react"
import "./styles.scss"

const AddTeacherToggleVisibilityButton = ({ toggleVisibility }) => {
  return (
    <div className="add-teacher-hide-show-button" onClick={toggleVisibility}>
      Add teacher
    </div>
  )
}

export default AddTeacherToggleVisibilityButton
