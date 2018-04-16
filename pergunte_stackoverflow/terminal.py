class Terminal:
    def mount_output(for_output={}):
        header = "Endpoint: {}\nParameters: q={} ; sort={} ; site={} ; order={}\n".format(
            for_output["endpoint"],
            for_output["parameters"]["q"],
            for_output["parameters"]["sort"],
            for_output["parameters"]["site"],
            for_output["parameters"]["order"]
        )

        output = header + Terminal._mount_search_results(for_output["search_results"])
        return output

    def _mount_search_results(search_results):
        output = ""

        for question in search_results:
            output = output + "=========================================================\n{}\n\nAnswer with higher score:\nSource: {}\n{}\n".format(
                question.title,
                question.best_answer.link,
                question.best_answer.body
            )

        return output
