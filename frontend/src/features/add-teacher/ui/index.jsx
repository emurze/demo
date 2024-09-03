import React, { useState } from "react"
import "./styles.scss"
import AddTeacherForm from "./form"
import AddTeacherToggleVisibilityButton from "./toggle-visibility-button"

const AddTeacher = () => {
  const [isVisible, setIsVisible] = useState(false)

  return (
    <div className="add-teacher">
      <AddTeacherToggleVisibilityButton
        toggleVisibility={() => setIsVisible(!isVisible)}
      />
      <AddTeacherForm isVisible={isVisible} />
    </div>
  )
}

export default AddTeacher
