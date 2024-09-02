import React from "react"
import "./styles.scss"

const SubjectDifficulty = ({ difficulty }) => {
  const formattedDifficulty = difficulty || "Не наю"
  return (
    <section className="subject-difficulty">
      Сложность: {formattedDifficulty}
    </section>
  )
}

export default SubjectDifficulty
