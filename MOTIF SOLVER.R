dna_sequence <- c()
motif <- "TAGC"

find_motifs <- function(sequence, motif) {
  motif_positions <- gregexpr(motif, sequence)
  positions <- as.integer(unlist(motif_positions))
  return(positions)
}

motif_positions <- find_motifs(dna_sequence, motif)
print(motif_positions)