import React from "react"
import "./styles.scss"
import TeacherDescription from "./teacher-description"
import TeacherSubjects from "./teacher-subjects"
import TeacherName from "./teacher-name"

const TeacherCard = (props) => {
  return (
    <div className="teacher-card">
      <TeacherName className="teacher-card__title" name={props.name} />
      <TeacherSubjects
        className="teacher-card__subjects"
        subjects={props.subjects}
      />
      <TeacherDescription
        className="teacher-card__description"
        negativeClassName="teacher-card__description-negative"
        description={props.description}
        rating={props.rating}
      />
    </div>
  )
}

export default TeacherCard
