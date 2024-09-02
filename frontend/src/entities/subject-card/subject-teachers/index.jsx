import React from "react"
import "./styles.scss"

const SubjectTeachers = ({ teachers }) => {
  return (
    <section className="subject-teachers">
      <div>Преподы:</div>
      <ul>
        {teachers.map((teacher, idx) => (
          <li className="teacher-card__item">
            {teacher}
            {idx !== teachers.length - 1 ? ", " : ""}
          </li>
        ))}
      </ul>
    </section>
  )
}

export default SubjectTeachers
