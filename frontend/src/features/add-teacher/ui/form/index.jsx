import React, { useState } from "react"
import "./styles.scss"
import { backendOrigin } from "../../../../app/constants"
import axios from "axios"

const AddTeacherForm = ({ isVisible }) => {
  const initialFormData = {
    title: "",
    description: "",
    difficulty: "",
  }

  const [formData, setFormData] = useState(initialFormData)

  const handleSubmit = (event) => {
    event.preventDefault()

    axios
      .post(backendOrigin + "/teachers/", formData)
      .then((resp) => console.log(resp))

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
      className={`add-teacher-form${isVisible ? " add-teacher-form-extended" : ""}`}
    >
      <input
        type="text"
        name="title"
        placeholder="Name"
        value={formData.title}
        onChange={handleChange}
        required
      />
      <input
        type="text"
        name="description"
        placeholder="Description"
        value={formData.description}
        onChange={handleChange}
        required
      />
      <select
        name="difficulty"
        value={formData.difficulty}
        onChange={handleChange}
        required
      >
        <option value="easy">Easy</option>
        <option value="normal">Normal</option>
        <option value="hard">Hard</option>
      </select>
      <button type="submit">Add</button>
    </form>
  )
}

export default AddTeacherForm
