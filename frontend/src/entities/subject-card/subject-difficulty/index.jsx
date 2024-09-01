import React from "react"
import "./styles.scss"

const SubjectDifficulty = ({ difficulty }) => {
  return (
    <div className="subject-difficulty">
      <div className="subject-card__title">Сложность:</div>
      <div className="subject-card__item">{difficulty}</div>
    </div>
  )
}

export default SubjectDifficulty
