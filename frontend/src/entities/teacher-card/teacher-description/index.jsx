import React from "react"
import "./styles.scss"

const TeacherDescription = ({
  description,
  rating,
  className,
  negativeClassName,
}) => {
  const IsPositive = rating > 5
  return (
    <div className={IsPositive ? className : negativeClassName}>
      {description}
    </div>
  )
}

export default TeacherDescription
