module CsvHeaderService
  extend self

  def csv_header_2(phases)
    header = [
      "S/N", "UUID", "Greenhouse Candidate ID", "Name", "E-mail", "Gender",
      "Location", "Program", "Start Date", "Language Stack", "Cycle",
      "Wk 1 LFA", "Wk 2 LFA", "Wk 1 Status", "Decision 1 Reason",
      "Decision 1 Comments", "Wk 2 Status", "Decision 2 Reason",
      "Decision 2 Comments", "Overall Avg", "Values Avg", "Output Avg",
      "Feedback Avg"
    ]

    # append holistic evaluation criteria
    HolisticEvaluation.max_evaluations.times do
      header.concat [
        "Quality", "Quantity", "Initiative", "Communication", "Integration",
        "EPIC", "Learning Ability"
      ]
    end

    phases.each do |phase|
      header.concat phase.assessments.map(&:name)
    end

    header
  end

  def csv_header_1(phases)
    header = %w[Biodata Biodata Biodata Biodata Biodata Biodata Biodata
                Biodata Biodata Biodata Biodata Biodata Decisions Decisions
                Decisions Decisions Decisions Decisions Decisions
                Critical-Numbers Critical-Numbers Critical-Numbers
                Critical-Numbers]

    HolisticEvaluation.max_evaluations.times do |i|
      7.times { header << "Holistic Evaluation #{i + 1}" }
    end

    phases.each { |phase| phase.assessments.each { header << phase.name } }

    header
  end
end
