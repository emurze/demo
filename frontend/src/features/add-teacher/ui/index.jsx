import React, { useState } from "react"
import "./styles.scss"

const AddTeacher = () => {
  const [formData, setFormData] = useState({
    name: "",
    subjects: [],
    description: "",
    rating: 1,
  })

  return (
    <div className="add-teacher">
      <div className="add-teacher__title">Add Teacher</div>
      <form className="add-teacher__form hidden"></form>
    </div>
  )
}

export default AddTeacher
