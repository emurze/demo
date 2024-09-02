import React from "react"
import "./styles.scss"

const AddTeacherToggleVisibilityButton = ({ toggleForm, isFormVisible }) => {
  return (
    <div className="add-teacher-hide-show-button" onClick={toggleForm}>
      Add teacher
    </div>
  )
}

export default AddTeacherToggleVisibilityButton
