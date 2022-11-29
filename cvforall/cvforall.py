import argparse


def easily_make_parser(description: str,
                       **kwargs) -> argparse.Namespace:
  """
  Helps to make arguments for starting script in command line
   in more friendly manner (using argparse library).

  Just put script description and all the flags you want to use
  when running the current program from the command line.

  This information will be accessible with "python3 script_name -h".

  :param description: shortly explains in command line how the script works
  :param kwargs: unlimited quantity of flags and their description
  :return: Namespace object from attributes parsed out of the command line
  """
  parser = argparse.ArgumentParser(description=description)

  for parser_argument_name, parser_argument_explanation in kwargs.items():
    parser.add_argument(f"--{parser_argument_name}", help=parser_argument_explanation)

  command_line_arguments = parser.parse_args()

  return command_line_arguments
