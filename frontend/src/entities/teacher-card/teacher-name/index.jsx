import React from "react"
import "./styles.scss"

const TeacherName = ({ name, className }) => {
  return <h3 className={className}>{name}</h3>
}

export default TeacherName
