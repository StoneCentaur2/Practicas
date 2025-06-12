const createRating = ({
    rating,
    total = 5,
    starIcon = '*', // puntuación rellena
    emptyIcon = '¤' // puntuación cuando estan vacias
}) => {
    const starts = starIcon.repeat(rating)
    const empty = emptyIcon.repeat(total - rating)

    return starts + empty
}