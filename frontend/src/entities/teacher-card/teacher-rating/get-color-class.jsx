const getColorClass = (rating, colors) => {
  if (rating) {
    if (rating >= 7 && rating <= 10) {
      return colors.get("Great")
    } else if ([5, 6].includes(rating)) {
      return colors.get("Acceptable")
    } else if (rating >= 1 && rating <= 4) {
      return colors.get("Unacceptable")
    } else {
      throw new Error("Rating must be from 1 to 10")
    }
  }
  return ""
}

export default getColorClass
