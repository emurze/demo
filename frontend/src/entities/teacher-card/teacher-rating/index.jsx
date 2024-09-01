import React from "react"
import "./styles.scss"
import getColorClass from "./get-color-class"

const TeacherRating = ({ rating }) => {
  const colorsMap = new Map([
    ["Great", "great-color"],
    ["Acceptable", "acceptable-color"],
    ["Unacceptable", "unacceptable-color"],
  ])
  const colorClass = getColorClass(rating, colorsMap)

  return (
    <section className={"teacher-rating"}>
      <div className="teacher-card__title">Рейтинг:</div>
      <div className={"teacher-card__item " + colorClass}>
        {rating || "ныту"}
      </div>
    </section>
  )
}

export default TeacherRating
