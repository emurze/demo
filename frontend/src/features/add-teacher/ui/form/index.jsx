import React, { useState } from "react"
import "./styles.scss"

const AddTeacherForm = ({ isFormVisible }) => {
  const initialFormData = {
    name: "",
    subjects: [],
    description: "",
    rating: 1,
  }

  const [formData, setFormData] = useState(initialFormData)

  const handleSubmit = (event) => {
    event.preventDefault()
    console.log("Form Data Submitted")
    console.log(formData)

    setFormData(initialFormData)
  }

  const handleChange = (event) => {
    const { name, value } = event.target
    setFormData({
      ...formData,
      [name]: value,
    })
  }

  return (
    // todo: connect csrf_token
    <form
      onSubmit={handleSubmit}
      className={`add-teacher-form${isFormVisible ? " add-teacher-form-extended" : ""}`}
    >
      <input
        type="text"
        name="name"
        placeholder="Name"
        value={formData.name}
        onChange={handleChange}
        required // ?
      />
      <input
        type="text"
        name="description"
        placeholder="Description"
        value={formData.description}
        onChange={handleChange}
        required
      />
      <input
        type="text"
        name="subjects"
        placeholder="Subjects"
        value={formData.subjects}
        onChange={handleChange}
      />
      <button type="submit">Add</button>
    </form>
  )
}

export default AddTeacherForm
