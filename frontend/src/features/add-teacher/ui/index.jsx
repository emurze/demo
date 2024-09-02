import React, { useState } from "react"
import "./styles.scss"
import AddTeacherForm from "./form"
import AddTeacherToggleVisibilityButton from "./toggle-visibility-button"

const AddTeacher = () => {
  const [isFormVisible, setFormVisible] = useState(false)

  return (
    <div className="add-teacher">
      <AddTeacherToggleVisibilityButton
        isFormVisible={isFormVisible}
        toggleForm={() => setFormVisible(!isFormVisible)}
      />
      <AddTeacherForm isFormVisible={isFormVisible} />
    </div>
  )
}

export default AddTeacher
