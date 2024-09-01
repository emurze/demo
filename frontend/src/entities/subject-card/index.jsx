import React from "react"
import "./styles.scss"
import SubjectTitle from "./subject-title"
import SubjectDifficulty from "./subject-difficulty"
import SubjectTeachers from "./subject-teachers"

const SubjectCard = (props) => {
  return (
    <div className="subject-card">
      <SubjectTitle title={props.title} />
      <SubjectTeachers teachers={props.teachers} />
      <SubjectDifficulty difficulty={props.difficulty} />
    </div>
  )
}

export default SubjectCard
