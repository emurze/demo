import React from "react"
import "./styles.scss"

const TeacherName = ({ name }) => {
  return (
    <section className="teacher-name">
      <div className="teacher-card__title">Имя: </div>
      <div className="teacher-card__item">{name}</div>
    </section>
  )
}

export default TeacherName
