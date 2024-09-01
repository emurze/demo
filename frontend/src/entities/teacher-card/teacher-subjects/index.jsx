import React from "react"
import "./styles.scss"

const TeacherSubjects = ({ subjects }) => {
  return (
    <section className="teacher-subjects">
      <div>Предметы:</div>
      <ul>
        {subjects.map((subject, idx) => (
          <li className="teacher-card__item">
            {subject}
            {idx !== subjects.length - 1 ? ", " : ""}
          </li>
        ))}
      </ul>
    </section>
  )
}

export default TeacherSubjects
