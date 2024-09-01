import React from "react"
import "./styles.scss"

const TeacherDescription = ({ description }) => {
  const truncateText = (text, maxLength) => {
    if (text.length > maxLength) {
      return text.slice(0, maxLength) + "..."
    }
    return text
  }
  const newDescription = description || "ныту"

  return (
    <section className="teacher-description">
      Описание: {truncateText(newDescription, 250)}
    </section>
  )
}

export default TeacherDescription
