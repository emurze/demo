import React from "react"
import "./styles.scss"
import SubjectTitle from "./subject-title"
import SubjectDifficulty from "./subject-difficulty"
import SubjectTeachers from "./subject-teachers"

const SubjectCard = ({ subject }) => {
  return (
    <div className="subject-card">
      <SubjectTitle title={subject.title} />
      <SubjectTeachers teachers={subject.teachers} />
      <SubjectDifficulty difficulty={subject.difficulty} />
    </div>
  )
}

export default SubjectCard
